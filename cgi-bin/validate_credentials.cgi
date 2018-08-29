use CGI;
use CGI::Session;
use CGI::Carp qw (fatalsToBrowser);

my $q = new CGI;
my $cookie_sid = $q->cookie('jadrn020SID');
my $session = new CGI::Session(undef, $cookie_sid, {Directory=>'/tmp'});
my $sid = $session->id;

if($cookie_sid ne $sid) {
    $response = "Authentication failed";
} else {
    $response = "OK";
}
print "Content-type: text/html\n\n";
print $response;