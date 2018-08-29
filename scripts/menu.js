var imageName = "";
var isNewInputValid = true;
var isAuthenticated = false;

/*Code developed by Mallikarjun, Pradeep
Project 1
Spring 2018
Username : jadrn020,
RED ID : 822032361*/

function resetAddForm() {
    form = document.getElementById("add-form");
    form.reset();
}

function resetEditForm() {
    form = document.getElementById("edit-form");
    form.reset();
}

$(document).ready(function () {

    $.get("/perl/jadrn020/validate_credentials.cgi", validateCredentials);
    hideStatus();

    $('#form-login').submit('click', function (event) {

        event.preventDefault();
        var uname = $("#input-username").val();
        var pwd = $("#input-password").val();

        data = $("#form-login").serialize();
        $.post("/perl/jadrn020/login.cgi", data, onLogin);
    });


    function onLogin(response) {

        if (response == "OK") {
            $('#login-container').hide();
            $('#menu-container').show();
            $('#login-error').hide();
        } else {
            $('#menu-container').hide();
            $('#login-error').show();
            $('#error-status').text("Invalid Credentials!");
        }
    }


    function validateCredentials(response) {

        if (response == "OK") {
            $('#login-container').hide();
            $('#menu-container').show();
            $('#login-error').hide();
            isAuthenticated = true;
        }
        else {
            $('#menu-container').hide();
            $('#login-container').show();
            $('#login-error').hide();
            $("#input-username").focus();
            isAuthenticated = false;
        }
    }


    $("#add-form").submit(function (e) {
        e.preventDefault();
        var data = new FormData(this);

        if (isNewInputValid) {

            $.ajax({
                url: "/perl/jadrn020/add_to_inventory.cgi",
                type: "post",
                data: data,
                processData: false,
                contentType: false,
                success: function () {
                    showStatus("Product added to the Inventory");
                    resetAddForm();
                },
                error: function (response) {
                    showStatus("Error inserting the product!!");
                }
            });
        } else {
            showStatus("Please enter a valid SKU")
        }
    });

    $("#edit-form").submit(function (e) {
        e.preventDefault();
        $('#edit-sku').prop('disabled', false);
        var data = new FormData(this);

        if (isNewInputValid) {

            $.ajax({
                url: "/perl/jadrn020/edit_inventory.cgi",
                type: "post",
                data: data,
                processData: false,
                contentType: false,
                success: function (response) {

                    if(response == "OK"){
                        showStatus("Product updated in the Inventory");
                        resetEditForm();
                        $('#e-image').prop('src', "./images/placeholder.png");
                    } else {
                        showStatus("Error updating the product!!");
                    }
                },
                error: function () {
                    showStatus("Error updating the product!!");
                }
            });
        } else {
            showStatus("Please enter a valid SKU");
        }
    });

    $('#delete-submit').on('click', function () {

        formData = new FormData();
        formData.append("sku", $('#delete-sku').val());
        formData.append("del-image-name", $('#del-image-name').val());

        if (isEmpty(sku)) {
            showStatus("Please enter the SKU");
            return;
        }

        $.ajax({
            url: "/perl/jadrn020/delete_inventory.cgi",
            type: "post",
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                if(response == "OK"){
                    showStatus("Product deleted Successfully");
                    resetDeleteForm();
                } else {
                    showStatus("Product not present in the Inventory");
                }

            },
            error: function () {
                showStatus("Product not present in the Inventory");
            }
        });
    });

    $('#manufacturer-id').on('blur', function () {

        var manufacturerID = $('#manufacturer-id').val();
        if (isEmpty(manufacturerID)) {
            showStatus("Please enter the Manufacturers Identifier");
            return;
        }
    });

    $('#description').on('blur', function () {

        var desc = $('#description').val();
        if (isEmpty(desc)) {
            showStatus("Please enter the product description");
            return;
        }
    });

    $('#cost').on('blur', function () {

        var cost = $('#cost').val();
        if (isEmpty(cost)) {
            showStatus("Please enter the product cost");
            return;
        }
    });

    $('#retail').on('blur', function () {

        var retail = $('#retail').val();
        if (isEmpty(retail)) {
            showStatus("Please enter the retail cost");
            return;
        } else {
            var cost = $('#cost').val();
            if (isEmpty(cost)) {
                showStatus("Please enter the product cost");
            } else if (retail < (1.25 * cost))
                showStatus("Please set the retail price 25% above cost price");
        }
    });


    $('#delete-tab').on('click', function () {
        $('#delete-sku').focus();
    });

    $('#edit-tab').on('click', function () {
        $('#edit-sku').focus();
    });


    $('#quantity').on('blur', function () {

        var quantity = $('#quantity').val();
        if (!isEmpty(quantity)) {
            if (quantity <= 0) {
                showStatus("Quantity must be greater than zero");
                return;
            }
        } else {
            showStatus("Please enter the Quantity");
        }
    });

    $('#features').on('blur', function () {

        var desc = $('#features').val();
        if (isEmpty(desc)) {
            showStatus("Please enter the product features");
        }
    });

    $('#edit-sku').on('blur', function () {

        $.get("/perl/jadrn020/validate_credentials.cgi", validateCredentials);
        if (isAuthenticated) {

            var sku = $('#edit-sku').val();
            if (validateSKU(sku)) {
                var urlNew = "/perl/jadrn020/fetch_data.cgi?sku=" + sku;
                $.get(urlNew, handleJsonData);
            } else {
                showStatus("Please enter a valid SKU");
                isNewInputValid = false;
            }
        }
    });


    $('#delete-sku').on('blur', function () {

        $.get("/perl/jadrn020/validate_credentials.cgi", validateCredentials);
        if (isAuthenticated) {

            var sku = $('#delete-sku').val();
            if (!sku) return;
            if (validateSKU(sku)) {
                $('#delete-submit').prop('disabled', false);
                var urlNew = "/perl/jadrn020/fetch_data.cgi?sku=" + sku;
                $.get(urlNew, handleJsonDataForDelete);
            } else {
                showStatus("Please enter a valid SKU");
                $('#delete-submit').prop('disabled', true);
            }
        }
    });

    $('#sku').on('blur', function () {

        $.get("/perl/jadrn020/validate_credentials.cgi", validateCredentials);

        if (isAuthenticated) {

            var sku = $('#sku').val();
            if (isEmpty(sku)) {
                showStatus("Please enter the SKU");
                isNewInputValid = false;
                return;
            } if (validateSKU(sku)) {
                $('#submit-add').prop('disabled', false);
                var urlNew = "/perl/jadrn020/check_duplicate.cgi?sku=" + sku;
                $.get(urlNew, processReply);
                isNewInputValid = true;
            } else {
                showStatus("Please enter a valid SKU");
                $('#submit-add').prop('disabled', true);
                isNewInputValid = false;
            }
        }

    });


    $("#product-image").change(function () {
        var input = this;
        imageName = input.files[0].name;
            if (input.files && input.files[0]) {
                var reader = new FileReader();

                reader.onload = function (e) {
                    $('#display-image')
                        .attr('src', e.target.result);
                };
                imageName = input.files[0].name;
                reader.readAsDataURL(input.files[0]);
            }
    });

    $("#edit-image").change(function () {
        var input = this;

            if (input.files && input.files[0]) {
                var reader = new FileReader();

                reader.onload = function (e) {
                    $('#e-image')
                        .attr('src', e.target.result);
                };
                imageName = input.files[0].name;
                reader.readAsDataURL(input.files[0]);
            }
    });

});

function validateSKU(sku) {
    return /^[a-zA-Z]{3}-\d{3}$/.test(sku);
};

function resetDeleteForm() {
    form = document.getElementById("delete-form");
    form.reset();
    $('#delete-image').prop('src', "./images/placeholder.png");
}

function isEmpty(fieldValue) {
    return $.trim(fieldValue).length == 0;
}

function isValidImage(imageName) {

    if ($('#product-image').val() != '') {
        return true;
    }
    else {
        showStatus("Please upload product image");
        return false;
    }

    var files = $('input[name=imageName]')[0].files;

    if (files.length == 0 || files[0].size == 0) {
        showStatus("Please upload the product Image")
        return;
    }
    if (files[0].size / 1000 > 3000) {
        showStatus("File size should be less than 3MB ");
    }
}

function showStatus(message) {
    $('#status-container').show();
    $('#status').text(message);
    setTimeout(clearStatus, 2000);
}

function hideStatus() {
    $('#status-container').hide();
    $('#status').text("");
}

function processReply(response) {

    if (response == "DUPLICATE") {
        showStatus("Product already exists in the Inventory");
        $('#submit-add').prop('disabled', true);
    } else {
        $('#submit-add').prop('disabled', false);
    }
}

function clearStatus() {
    $('#status-container').fadeOut(2000);
}

function handleJsonData(response) {
    if (response == "Error") {
        isNewInputValid = false;
        showStatus("Please enter a valid SKU")
        return;
    }
    isNewInputValid = true;
    $('#edit-sku').prop('disabled', true);
    var keys = ['#edit-sku', '#edit-category', '#edit-vendor', '#edit-manufacturer-id', '#edit-description', '#edit-cost', '#edit-retail', '#edit-quantity', '#edit-features'];
    var obj_data = eval("(" + response + ")");
    for (i = 0; i < obj_data.length; i++) {
        for (j = 0; j < obj_data[i].length; j++)
            $(keys[j]).val(obj_data[i][j]);
    }
    $('#e-image').prop('src', "/~jadrn020/file_upload/_uploadDIR_/" + obj_data[0][9] + '?' +new Date().getTime());
}

function handleJsonDataForDelete(response) {
    if (response == "Error") {
        showStatus("Please enter a valid identifier");
        return;
    }
    var keys = ['#delete-sku', '#delete-category', '#delete-vendor', '#delete-manufacturer-id', '#delete-description', '#delete-cost', '#delete-retail', '#delete-quantity', '#delete-features', '#del-image-name'];
    var obj_data = eval("(" + response + ")");
    for (i = 0; i < obj_data.length; i++) {
        for (j = 0; j < obj_data[i].length; j++)
            $(keys[j]).val(obj_data[i][j]);
    }
    $('#delete-image').prop('src', "/~jadrn020/file_upload/_uploadDIR_/" + obj_data[0][9]);
}











