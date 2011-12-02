function expandSelected(event, selectorName) {
    function getExtraForValue(value) {
	return $('#form-' + value + '-extra');
    }
    var select = $(selectorName)[0];
    var selectedValue = select.value;
    for (i = 0; i < select.children.length; ++i) {
	var currentValue = select.children[i].value;
	if (currentValue != selectedValue)
	    getExtraForValue(currentValue).hide();
    }
    getExtraForValue(selectedValue).show();
}

function validateField(event, fieldName, regex) {
    var field = $(fieldName);
    if (field.val().match(regex) == null) {
	event.preventDefault();
	field.addClass('form-error');
    }
}