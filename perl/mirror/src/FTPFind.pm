package FTPFind;
use strict;

use vars qw($VERSION @ISA @EXPORT);
use Exporter;
$VERSION = 1.00;
@ISA = qw (Exporter);
@EXPORT = qw(ftp_finddepth);


sub ftp_finddepth {

    my ($ftp, $callback, $level) = @_;

    # Make a listing of files and/or directories.
    my @files = $ftp->dir
        or die "ERROR: dir() failed\n";

    foreach my $i (@files) {

        my @items = split(/\s/, $i);
        my $item = $items[$#items];

        my $parent = $ftp->pwd;

        if ($i =~ /^d(.*)/) {

            # Skip . and .. if present in the listing.
            # (Some FTP servers list these, some don't.)
            next if $item =~ /\.\.?$/;

            # It's a directory - call the callback.
            &$callback($level, 1, $item, $parent);
            
            # Recursively crawl the subtree under this directory.
            $ftp->cwd($item)
                or die "ERROR: can't cwd() to $item\n";
            ftp_finddepth($ftp, $callback, $level+1);

            # Restore location in remote tree.
            $ftp->cwd($parent)
                or die "ERROR: can't cwd() to $parent\n";
        } 
        elsif ($i =~ /^-(.*)/) {

            # It's a file - call the callback.
            &$callback($level, 0, $item, $parent);
        }
    }
}

1;
