#!/usr/bin/perl

use DBI;
use CGI;
my $q = new CGI;
my $sku = $q->param('sku');

my $host = 'opatija.sdsu.edu';
my $port = '3306';
my $database = 'jadrn020';
my $username = 'jadrn020';
my $password = 'desktop';

my $database_source = "dbi:mysql:$database:$host:$port";
my $dbh = DBI->connect($database_source, $username, $password)
    or die "Cannot connect to DB";


my $query = "select sku, catID, venID, manufacturerID, description, cost, retail, quantity, features, image from product where sku='$sku'";
my $sth = $dbh->prepare($query);
$sth->execute();

if($sth->rows == 0){
    $response = 'Error';
} else {
    $response = '';
    $response .= '[';
    while(my @row=$sth->fetchrow_array()) {
        $response .= "[";
        foreach $item (@row) {
            $response .= '\''.$item . '\',';
        }
        $response = substr $response, 0, (length($response)-1);
        $response .= '],';
    }
    $response = substr $response, 0, (length($response)-1);
    $response .= ']';
}



unless($response) {
    $response = "invalid";
}

$sth->finish();
$dbh->disconnect();

print "Content-type: text/html\n\n";
print $response;