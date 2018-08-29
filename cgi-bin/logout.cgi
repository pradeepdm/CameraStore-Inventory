use CGI;
use CGI::Session;
use CGI::Carp qw (fatalsToBrowser);

my $q = new CGI;
my $sid = $q->cookie("jadrn020SID") || undef;
$session = new CGI::Session(undef, $sid, {Directory => '/tmp'});
$session->delete();
my $cookie = $q->cookie(jadrn020SID => '');
print $q->header( -cookie=>$cookie ); #send cookie with session ID to browser  


print <<END;
    
<!DOCTYPE html>
<html>

<head>
    <title>Login</title>
    <meta http-equiv="content-type" content="text/html;charset=utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <META HTTP-EQUIV="Cache-Control" CONTENT="no-cache, no-store, must-revalidate" />
    <META HTTP-EQUIV="Pragma" CONTENT="no-cache" />
    <META HTTP-EQUIV="Expires" CONTENT="0" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="http://jadran.sdsu.edu/~jadrn020/proj1/styles/styles.css"/>
    <link rel="stylesheet" type="text/css" href="http://jadran.sdsu.edu/~jadrn020/proj1/styles/menu.css"/>
    <script src="http://jadran.sdsu.edu/jquery/jquery.js"></script>
    <script src="http://jadran.sdsu.edu/jquery/jQueryUI.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="http://jadran.sdsu.edu/~jadrn020/proj1/scripts/menu.js"></script>
    <link href="https://www.fontify.me/wf/a899c3e7c4d07950ac58db0ee10c33f0" rel="stylesheet" type="text/css">
</head>

<body>
<div id="login-container">
    <div id="left-panel">
        <form class="form-signin" id="form-login" action="" method="post">
            <h2 class="form-signin-heading">Sign in</h2>
            <label for="input-username" class="sr-only">User name</label>
            <input type="text" name="input-username" id="input-username" class="form-control" placeholder="User name" required autofocus>
            <label for="input-password" class="sr-only">Password</label>
            <input type="password" name="input-password" id="input-password" class="form-control" placeholder="Password" required>
            <button id="login-submit" class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
        </form>
        <div id="login-error" class="alert alert-info" role="alert">
            <strong id="error-status"></strong>
        </div>
    </div>
    <div id="right-panel"></div>
</div>
<div id="menu-container">
    <nav id="header-nav" class="navbar navbar-inverse navbar-static-top" role="navigation">
        <div  class="container">

            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".nav-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#"><strong class="header-text">Camera</strong></a>
            </div>

            <div class="collapse navbar-collapse">
                <ul class="nav navbar-nav navbar-right">
                    <li>
                        <a href="http://jadran.sdsu.edu/perl/jadrn020/logout.cgi"><strong class="header-text">Logout</strong></a>
                    </li>
                </ul>
            </div>

        </div>
    </nav>
    <div class="container">
        <div id="tab-container" class="container">
            <div id="status-container" class="alert alert-info" role="alert">
                <strong id="status" ></strong>
            </div>
            <ul class="nav nav-pills">
                <li class="active">
                    <a href="#1b" data-toggle="tab">New Record</a>
                </li>
                <li><a href="#2b" data-toggle="tab" id="edit-tab">Edit Record</a>
                </li>
                <li><a href="#3b" data-toggle="tab" id="delete-tab">Delete Record</a>
                </li>
            </ul>
            <div class="tab-content clearfix" id="tabs">
                <div class="tab-pane active" id="1b">
                    <form id = "add-form">
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="sku">SKU</label>
                                    <input type="text" class="form-control" placeholder="" name="sku" id="sku" required>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="category">Category</label>

                                    <select class="form-control" name="category" id="category" required>
                                        <option value="1">DSLR</option>
                                        <option value="2">Point and Shoot</option>
                                        <option value="3">Advanced Amateur</option>
                                        <option value="4">Underwater</option>
                                        <option value="5">Film</option>
                                        <option value="6">mirrorless</option>
                                        <option value="7">superzoom</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="vendor">Vendor</label>
                                    <select class="form-control" name="vendor" id="vendor" required>
                                        <option value="1">Nikon</option>
                                        <option value="2">Canon</option>
                                        <option value="3">Olympus</option>
                                        <option value="4">Lumix</option>
                                        <option value="5">Pentax</option>
                                        <option value="6">Leica</option>
                                        <option value="7">Sony</option>
                                        <option value="8">Fuji</option>
                                    </select>
                                </div>
                            </div>

                            <div class="col-md-6">

                                <div class="form-group">
                                    <label for="manufacturer-id">Manufacturer's Identifier</label>
                                    <input type="text" class="form-control" name="manufacturer-id" id="manufacturer-id" placeholder="Identifier" required>
                                </div>
                            </div>
                            <!--  col-md-6   -->
                        </div>
                        <div class="row">
                            <div class="col-md-6">

                                <div class="form-group">
                                    <label for="description">Description</label>
                                    <input type="text" class="form-control" id="description" name="description"
                                           placeholder="Enter the Description" required>
                                </div>

                            </div>

                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="cost">Cost</label>
                                    <input type="number" class="form-control" name="cost" placeholder="Enter the Cost price" id="cost" required>
                                </div>
                            </div>


                        </div>
                        <div class="row">

                            <!--  col-md-6   -->
                            <div class="col-md-6">

                                <div class="form-group">
                                    <label for="retail">Retail</label>
                                    <input type="number" class="form-control" name="retail" id="retail" placeholder="Enter the Retail price" required>
                                </div>
                            </div>

                            <!--  col-md-6   -->
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="quantity">Quantity</label>
                                    <input type="number" class="form-control" name="quantity" placeholder="Quantity must be greater than zero"
                                           id="quantity" required>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="features">Features</label>
                                    <textarea class="form-control" rows="3" placeholder="Enter the features" name="features"
                                              id="features" required></textarea>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <img id="display-image" alt="Product Image" src="http://jadran.sdsu.edu/~jadrn020/proj1/images/placeholder.png" />
                            </div>

                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="product-image">Product Image</label>
                                    <input type="file" class="form-control" id="product-image"
                                           name="product-image" accept="image/*" required>
                                </div>
                            </div>
                        </div>
                        <input type="submit" class="btn btn-primary" value="Submit" id="submit-add" />
                        <button type="reset" class="btn btn-primary" id="clear-add">Clear</button>
                    </form>
                </div>
                <div class="tab-pane" id="2b">
                    <form id = "edit-form" enctype="multipart/form-data">
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="edit-sku">SKU</label>
                                    <input type="text" class="form-control" placeholder="" name="edit-sku" id="edit-sku" required>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="edit-category">Category</label>

                                    <select class="form-control" name="edit-category" id="edit-category" required>
                                        <option value="1">DSLR</option>
                                        <option value="2">Point and Shoot</option>
                                        <option value="3">Advanced Amateur</option>
                                        <option value="4">Underwater</option>
                                        <option value="5">Film</option>
                                        <option value="6">mirrorless</option>
                                        <option value="7">superzoom</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="edit-vendor">Vendor</label>
                                    <select class="form-control" name="edit-vendor" id="edit-vendor" required>
                                        <option value="1">Nikon</option>
                                        <option value="2">Canon</option>
                                        <option value="3">Olympus</option>
                                        <option value="4">Lumix</option>
                                        <option value="5">Pentax</option>
                                        <option value="6">Leica</option>
                                        <option value="7">Sony</option>
                                        <option value="8">Fuji</option>
                                    </select>
                                </div>
                            </div>

                            <div class="col-md-6">

                                <div class="form-group">
                                    <label for="edit-manufacturer-id">Manufacturer's Identifier</label>
                                    <input type="text" class="form-control" name="edit-manufacturer-id" id="edit-manufacturer-id" placeholder="Identifier" required>
                                </div>
                            </div>
                            <!--  col-md-6   -->
                        </div>
                        <div class="row">
                            <div class="col-md-6">

                                <div class="form-group">
                                    <label for="edit-description">Description</label>
                                    <input type="text" class="form-control" id="edit-description" name="edit-description"
                                           placeholder="Enter the Description" required>
                                </div>

                            </div>

                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="edit-cost">Cost</label>
                                    <input type="number" class="form-control" name="edit-cost" placeholder="Enter the Cost price" id="edit-cost" required>
                                </div>
                            </div>


                        </div>
                        <div class="row">

                            <!--  col-md-6   -->
                            <div class="col-md-6">

                                <div class="form-group">
                                    <label for="edit-retail">Retail</label>
                                    <input type="number" class="form-control" name="edit-retail" id="edit-retail" placeholder="Enter the Retail price" required>
                                </div>
                            </div>

                            <!--  col-md-6   -->
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="edit-quantity">Quantity</label>
                                    <input type="number" class="form-control" name="edit-quantity" placeholder="Quantity must be greater than zero"
                                           id="edit-quantity" required>
                                </div>
                            </div>
                        </div>
                        <div class="row">


                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="edit-features">Features</label>
                                    <textarea class="form-control" rows="3" placeholder="Enter the features" name="edit-features"
                                              id="edit-features" required></textarea>
                                </div>

                            </div>
                            <div class="col-md-6">
                                <img id="e-image" alt="Product Image" src="http://jadran.sdsu.edu/~jadrn020/proj1/images/placeholder.png"/>
                            </div>

                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="edit-image">Product Image</label>
                                    <input type="file" class="form-control" id="edit-image" name="edit-image"
                                           placeholder="Enter the Retail price" accept="image/*" required>
                                </div>
                            </div>
                        </div>
                        <input type="submit" class="btn btn-primary" value="Update" id="edit-submit" />
                        <button type="reset" class="btn btn-primary" id="edit-clear">Clear</button>
                    </form>
                </div>
                <div class="tab-pane" id="3b">
                    <form id = "delete-form" enctype="multipart/form-data">
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="delete-sku">SKU</label>
                                    <input type="text" class="form-control" placeholder="" name="delete-sku" id="delete-sku" required>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="delete-category">Category</label>

                                    <select class="form-control" name="delete-category" id="delete-category" required disabled>
                                        <option value="1">DSLR</option>
                                        <option value="2">Point and Shoot</option>
                                        <option value="3">Advanced Amateur</option>
                                        <option value="4">Underwater</option>
                                        <option value="5">Film</option>
                                        <option value="6">mirrorless</option>
                                        <option value="7">superzoom</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="delete-vendor">Vendor</label>
                                    <select class="form-control" name="delete-vendor" id="delete-vendor" required disabled>
                                        <option value="1">Nikon</option>
                                        <option value="2">Canon</option>
                                        <option value="3">Olympus</option>
                                        <option value="4">Lumix</option>
                                        <option value="5">Pentax</option>
                                        <option value="6">Leica</option>
                                        <option value="7">Sony</option>
                                        <option value="8">Fuji</option>
                                    </select>
                                </div>
                            </div>

                            <div class="col-md-6">

                                <div class="form-group">
                                    <label for="delete-manufacturer-id">Manufacturer's Identifier</label>
                                    <input type="text" class="form-control" name="delete-manufacturer-id"
                                    id="delete-manufacturer-id" placeholder="Identifier" required disabled>
                                </div>
                            </div>
                            <!--  col-md-6   -->
                        </div>
                        <div class="row">
                            <div class="col-md-6">

                                <div class="form-group">
                                    <label for="delete-description">Description</label>
                                    <input type="text" class="form-control" id="delete-description" name="delete-description"
                                           placeholder="Enter the Description" required disabled>
                                </div>

                            </div>

                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="delete-cost">Cost</label>
                                    <input type="number" class="form-control" name="delete-cost"
                                    placeholder="Enter the Cost price" id="delete-cost" required disabled>
                                </div>
                            </div>


                        </div>
                        <div class="row">

                            <!--  col-md-6   -->
                            <div class="col-md-6">

                                <div class="form-group">
                                    <label for="delete-retail">Retail</label>
                                    <input type="number" class="form-control" name="delete-retail" id="delete-retail"
                                    placeholder="Enter the Retail price" required disabled>
                                </div>
                            </div>

                            <!--  col-md-6   -->
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="delete-quantity">Quantity</label>
                                    <input type="number" class="form-control" name="delete-quantity" placeholder="Quantity must be greater than zero"
                                           id="delete-quantity" required disabled>
                                </div>
                            </div>
                        </div>
                        <div class="row">

                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="delete-features">Features</label>
                                    <textarea class="form-control" rows="3" placeholder="Enter the features" name="delete-features"
                                              id="delete-features" required disabled></textarea>
                                </div>

                            </div>
                            <div class="col-md-6">
                                <img id="delete-image" alt="Product Image" src="http://jadran.sdsu.edu/~jadrn020/proj1/images/placeholder.png"/>
                            </div>

                        </div>
                        <input type="button" class="btn btn-primary" value="Delete" id="delete-submit" />
                        <button type="reset" class="btn btn-primary" id="delete-clear">Clear</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
</body>

</html>

END