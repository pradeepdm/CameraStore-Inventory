use CGI;
use DBI;
use CGI::Carp qw (fatalsToBrowser);
use CGI::Session;

my $upload_dir = '/home/jadrn020/public_html/file_upload/_uploadDIR_';

my $q = new CGI;
my $sku = $q->param('sku');
my $filename = $q->param('del-image-name');

$filename = "$upload_dir/$filename";
unlink($filename);

my $host = 'opatija.sdsu.edu';
my $port = '3306';
my $database = 'jadrn020';
my $username = 'jadrn020';
my $password = 'desktop';
my $database_source = "dbi:mysql:$database:$host:$port";
my $dbh = DBI->connect($database_source, $username, $password)
    or die "Cannot connect to DB";

$query = "DELETE FROM product where sku = '$sku'";
my $sth = $dbh->prepare($query);
$sth->execute();

if($sth->rows == 0){
    $response = 'Error';
} else {
    $response = 'OK';
}

unless($response) {
    $response = "invalid";
}

$sth->finish();
$dbh->disconnect();

print "Content-type: text/html\n\n";
print $response;