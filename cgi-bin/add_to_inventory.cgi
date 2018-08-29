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
my $sku = $q->param('sku');
my $filename = $q->param("product-image");
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
my $fileHandle = $q->upload("product-image");
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

my $category = $q->param('category');
my $vendor = $q->param('vendor');
my $manID = $q->param('manufacturer-id');
my $description = $q->param('description');
my $features = $q->param('features');
my $cost = $q->param('cost');
my $retail = $q->param('retail');
my $quantity = $q->param('quantity');
my $image = $q->param('product-image');


my $host = 'opatija.sdsu.edu';
my $port = '3306';
my $database = 'jadrn020';
my $username = 'jadrn020';
my $password = 'desktop';
my $database_source = "dbi:mysql:$database:$host:$port";
my $dbh = DBI->connect($database_source, $username, $password)
    or die "Cannot connect to DB";

$query = "INSERT INTO product(sku, catID, venID, manufacturerID, description, features, cost, retail, quantity, image)
			VALUES ('$sku', '$category', '$vendor', '$manID', '$description', '$features', '$cost', '$retail', '$quantity', '$filename')";
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

