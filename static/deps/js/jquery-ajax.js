// Waiting document load
$(document).ready(function () {
    // Get notification by id for ajax notifications
    let successMessage = $("#jq-notification");


    // Event for <add to cart> button
    $(document).on("click", ".add-to-cart", function (e) {
        e.preventDefault();
        // Get cart items counter value
        let goodsInCartCount = $("#goods-in-cart-count");
        let cartCount = parseInt(goodsInCartCount.text() || 0);
        // Get id from attribute data-product-id
        let product_id = $(this).data("product-id");
        // Get href for django controller
        let add_to_cart_url = $(this).attr("href");
        // Make post req using ajax without page reload
        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Success message
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);
                // Increase cart items
                cartCount++;
                goodsInCartCount.text(cartCount);
                // Change cart content in response from django (new html part for cart)
                let cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);
            },
            error: function (data) {
                console.log("Error while adding item to cart");
            },
        });
    });


    // Event for <remove from cart> button
    $(document).on("click", ".remove-from-cart", function (e) {
        e.preventDefault();
        // Get cart items counter value
        let goodsInCartCount = $("#goods-in-cart-count");
        let cartCount = parseInt(goodsInCartCount.text() || 0);
        // Get id from attribute data-product-id
        let cart_id = $(this).data("cart-id");
        // Get href for django controller
        let remove_from_cart = $(this).attr("href");
        // Make post req using ajax without page reload
        $.ajax({
            type: "POST",
            url: remove_from_cart,
            data: {
                cart_id: cart_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Success message
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);
                // Decrease cart items
                cartCount -= data.quantity_deleted;
                goodsInCartCount.text(cartCount);
                // Change cart content in response from django (new html part for cart)
                let cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);
            },
            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });


    // Event for <-> button
    $(document).on("click", ".decrement", function () {
        // Get href for django controller from data-cart-change-url attribute
        let url = $(this).data("cart-change-url");
        // Get cart id from data-cart-id attribute
        let cartID = $(this).data("cart-id");
        // Get near input with cart items count
        let closestInput = $(this).closest('.input-group').find('.number');
        // Get current items count from cart
        let currentValue = parseInt(closestInput.val());
        // Decrease cart items count only if items amount more than 1
        if (currentValue > 1) {
            closestInput.val(currentValue - 1);
            // Update items in cart
            updateCart(cartID, currentValue - 1, -1, url);
        }
    });


    // Event for <+> button
    $(document).on("click", ".increment", function () {
        // Get href for django controller from data-cart-change-url attribute
        let url = $(this).data("cart-change-url");
        // Get cart id from data-cart-id attribute
        let cartID = $(this).data("cart-id");
        // Get near input with cart items count
        let closestInput = $(this).closest('.input-group').find('.number');
        // Get current items count from cart
        let currentValue = parseInt(closestInput.val());
        // Increase cart items count
        closestInput.val(currentValue + 1);
        // Update items in cart
        updateCart(cartID, currentValue + 1, 1, url);
    });


    // Function to update items count in cart
    function updateCart(cartID, quantity, change, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Success notification
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);
                // Change items amount in cart
                let goodsInCartCount = $("#goods-in-cart-count");
                let cartCount = parseInt(goodsInCartCount.text() || 0);
                cartCount += change;
                goodsInCartCount.text(cartCount);
                // Change cart content
                let cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);
            },
            error: function (data) {
                console.log("Error while adding to cart");
            },
        });
    }

    //  Get notification element by id
    let notification = $('#notification');
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 5000);
    }

    // Event for button <cart> (to show it)
    $('#modalButton').click(function () {
        let modalWindow = $('#exampleModal')
        modalWindow.appendTo('body');

        modalWindow.modal('show');
    });

    // Event for close cart (in modal window) button
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });


    // Events for delivery method radiobutton
    $("input[name='requires_delivery']").change(function () {
        let selectedValue = $(this).val();
        // Hide or show delivery address field
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });
    // To update delivery address state (show/hide) on page update
    let deliveryRadiobutton = $("input[id='id_requires_delivery_0']")
    deliveryRadiobutton.ready(function () {
        let selectedValue = $("input[id='id_requires_delivery_0']").is(":checked");
        // Hide or show delivery address field
        if (selectedValue === false) {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });
});