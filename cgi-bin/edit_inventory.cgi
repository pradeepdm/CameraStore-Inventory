use CGI;
use DBI;
use CGI::Carp qw (fatalsToBrowser);
use File::Basename;

####################################################################
### constants
$CGI::POST_MAX = 1024 * 3000; # Limit file size to 3MB
my $upload_dir = '/home/jadrn020/public_html/file_upload/_uploadDIR_';
my $safe_filename_chars = "a-zA-Z0-9_.-";
####################################################################

my $q = new CGI;
my $sku = $q->param('edit-sku');
my $filename = $q->param('edit-image');
unless ($filename) {
    die "There was a problem uploading the image; " .
            "it's probably too big.";
}

my ($name, $path, $extension) = fileparse($filename, '\.[^\.]*');
$filename = $sku.$extension;
$filename =~ s/ //; #remove any spaces
if ($filename !~ /^([$safe_filename_chars]+)$/) {
    die "Sorry, invalid character in the filename.";
}

$filename = untaint($filename);
# get a handle on the uploaded image
my $fileHandle = $q->upload("edit-image");
unless ($fileHandle) {
    die "Invalid handle";
}

# save the file
open UPLOADFILE, ">$upload_dir/$filename" or die
    "Error, cannot save the file.";
binmode UPLOADFILE;
while(<$fileHandle>) {
    print UPLOADFILE $_;
}
close UPLOADFILE;

my $category = $q->param('edit-category');
my $vendor = $q->param('edit-vendor');
my $manID = $q->param('edit-manufacturer-id');
my $description = $q->param('edit-description');
my $features = $q->param('edit-features');
my $cost = $q->param('edit-cost');
my $retail = $q->param('edit-retail');
my $quantity = $q->param('edit-quantity');


my $host = 'opatija.sdsu.edu';
my $port = '3306';
my $database = 'jadrn020';
my $username = 'jadrn020';
my $password = 'desktop';
my $database_source = "dbi:mysql:$database:$host:$port";
my $dbh = DBI->connect($database_source, $username, $password)
    or die "Cannot connect to DB";
$query = "UPDATE product SET catID='$category', venID='$vendor', manufacturerID='$manID', description='$description',
features='$features', cost='$cost', retail='$retail', quantity='$quantity' where sku='$sku'";
$statement = $dbh->prepare($query);
$statement->execute();

if ($statement->rows == 0) {
    $response = 'Error';
}
else {
    $response = 'OK';
}

$statement->finish();
$dbh->disconnect();

print "Content-type: text/html\n\n";
print $response;

sub untaint {
    if ($filename =~ m/^(\w+)$/) {die "Tainted filename!";}
    return $1;
}

