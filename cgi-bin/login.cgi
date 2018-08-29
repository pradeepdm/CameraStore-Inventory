use CGI;
use CGI::Session;
use CGI::Carp qw (fatalsToBrowser);
use Crypt::Password;

##---------------------------- MAIN ---------------------------------------

my $q;
if(authenticate_user()) {
    send_to_main();
    print "OK";
}
else {
    print "Invalid";
}

sub authenticate_user {
    $q = new CGI;
    my $user = $q->param("input-username");
    my $password = $q->param("input-password");
    open DATA, "</srv/www/cgi-bin/jadrn020/passwords.dat"
        or die "Cannot open file.";
    @file_lines = <DATA>;
    close DATA;

    $OK = 0; #not authorized

    foreach $line (@file_lines) {
        chomp $line;
        ($stored_user, $stored_pass) = split /=/, $line;
        if($stored_user eq $user && check_password($stored_pass, $password)) {
            $OK = 1;
            last;
        }
    }

    return $OK;
}

sub send_to_main {
    # args are DRIVER, CGI OBJECT, SESSION LOCATION
    # default for undef is FILE, NEW SESSION, /TMP
    # for login.html, don't look for any existing session.
    # Always start a new one.  Send a cookie to the browser.
    # Default expiration is when the browser is closed.
    # WATCH YOUR COOKIE NAMES! USE JADRNXXX_SID
    my $session = new CGI::Session(undef, undef, {Directory=>'/tmp'});
    $session->expires('+1d');
    my $cookie = $q->cookie(jadrn020SID => $session->id);
    print $q->header( -cookie=>$cookie ); #send cookie with session ID to browser
}