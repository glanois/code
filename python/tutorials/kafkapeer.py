""" 

Kafka peer mulithreaded python application.

See https://kafka.apache.org/quickstart


Step 1: Download the code
-------------------------

> tar -xzf kafka_2.12-2.3.1.tgz
> cd kafka_2.12-2.3.1


Step 2: Start the server
------------------------

Window 1:
> bin/zookeeper-server-start.sh config/zookeeper.properties

Window 2:
> bin/kafka-server-start.sh config/server.properties


Step 3: Create a topic
----------------------

Window 3:
> bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic demo

> bin/kafka-topics.sh --list --bootstrap-server localhost:9092


Step 4: Start a consumer
------------------------

Window 3:
> bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic demo


Step 5: Send some messages
--------------------------

Window 4:
> bin/kafka-console-producer.sh --broker-list localhost:9092 --topic demo

Type some text and press RETURN.

Notice that what you entered shows up in the consumer window you created
in the preceding step.


Step 6: Start some instances of this application
------------------------------------------------

Window 5:
> python3 kafkapeer.py 


Window 6:
> python3 kafkapeer.py 

.
.
.
Window <n>:
> python3 kafkapeer.py 

Step 7: Go to the producer window (Window 3) and enter some messages
--------------------------------------------------------------------

Window 3:
> hello
> marco
> marco
> marco
> ping
> ping
> marco
> ping
> stop

In the consumer window (Window 3), notice each of the messages 
you typed are received.  Also notice that each of the 'marco' and 
'ping' messages result in 'polo' and 'ping' messages (one response
from each of the kafkapeer.py instances you started in step 6 above).

"""

import sys
import argparse
import logging
import threading
import queue
import time
import kafka
import json


class Transmitter(threading.Thread):
    def __init__(self, q, server, port, topic):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()
        self._q      = q
        self._server = server
        self._port   = port
        self._topic  = topic
        
    def stop(self):
        self._stop_event.set()

    def run(self):
        producer = kafka.KafkaProducer(
            bootstrap_servers='%s:%s' % (self._server, self._port))
        while not self._stop_event.is_set():
            try:
                msg = self._q.get(timeout=1)
                producer.send(self._topic, msg)
            except queue.Empty:
                pass
        producer.close()


class Receiver(threading.Thread):
    def __init__(self, q, server, port, topic):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()
        self._q      = q
        self._server = server
        self._port   = port
        self._topic  = topic

    def stop(self):
        self._stop_event.set()
        
    def run(self):
        consumer = kafka.KafkaConsumer(
            bootstrap_servers='%s:%s' % (self._server, self._port),
            group_id=None,
            consumer_timeout_ms=1000)
        consumer.subscribe([ self._topic ])
        while not self._stop_event.is_set():
            for message in consumer:
                put = False
                retries = 0
                max_retries = 5
                while not put and retries < max_retries:
                    try:
                        self._q.put(message.value, timeout=1)
                        put = True
                    except queue.Full:
                        logging.warning('Receiver::run() - application queue is full, retrying.')

                if not put:
                    logging.error('Receiver::run() - failed to put incoming message onto application queue.')
        consumer.close()
        
        
class Application(threading.Thread):
    def __init__(self, server, port, topic):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()
        self._in_queue  = queue.Queue()
        self._out_queue = queue.Queue()
        self._threads = [
            Transmitter(self._out_queue, server, port, topic),
            Receiver(   self._in_queue,  server, port, topic) ]

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def process_message(self, msg):
        logging.info('Application::process_message() - got %s' % (msg.decode('utf-8')))

    def run(self):
        for t in self._threads:
            t.start()

        while not self._stop_event.is_set():
            try:
                msg = self._in_queue.get(timeout=1)
                self.process_message(msg)
            except queue.Empty:
                pass

        for t in self._threads:
            t.stop()

        for t in self._threads:
            t.join()


class MarcoPolo(Application):
    def __init__(self, server, port, topic):
        Application.__init__(self, server, port, topic)
        self._stopping = False

    def process_message(self, msg):
        msg = msg.decode('utf-8')
        if msg == 'marco':
            response = 'polo'
            self._out_queue.put(response.encode('utf-8'))
        elif msg == 'stop':
            self.stop()
        

class PingPong(Application):
    def __init__(self, server, port, topic):
        Application.__init__(self, server, port, topic)
        self._stopping = False

    def process_message(self, msg):
        msg = msg.decode('utf-8')
        if msg == 'ping':
            response = 'pong'
            self._out_queue.put(response.encode('utf-8'))
        elif msg == 'stop':
            self.stop()
        

def main(options):
    
    mp = MarcoPolo(options.server[0], options.port[0], options.topic[0])
    mp.start()

    pp = PingPong(options.server[0], options.port[0], options.topic[0])
    pp.start()

    while not mp.stopped() or not pp.stopped():
        time.sleep(1)

    mp.join()
    pp.join()

    return 0


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'server',
        help='Address of the server.',
        nargs=1)

    parser.add_argument(
        'port',
        help='Port of the server.',
        nargs=1)

    parser.add_argument(
        'topic',
        help='Topic to participate in.',
        nargs=1)

    options = parser.parse_args()
    sys.exit(main(options))
