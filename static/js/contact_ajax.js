$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#store-contact .modal-content").html("");
        $("#store-contact").modal("show");
      },
      success: function (data) {
        $("#store-contact .modal-content").html(data.html_form);
      }
    });
  };

  var sendForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#store-contact").modal("hide");
        }
        else {
          $("#store-contact .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // make contact
  $(".js-store-contact").click(loadForm);
  $("#store-contact").on("submit", ".js-book-create-form", sendForm);

});