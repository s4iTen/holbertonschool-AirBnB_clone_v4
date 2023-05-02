$(document).ready(function () {
  const amenities = {};

  // Listen for changes on each input checkbox tag
  $('input[type=checkbox]').change(function () {
    const amenityId = $(this).data('id');
    const amenityName = $(this).data('name');

    // If the checkbox is checked, store the Amenity ID in a variable
    if ($(this).is(':checked')) {
      amenities[amenityId] = amenityName;
    }
    // If the checkbox is unchecked, remove the Amenity ID from the variable
    else {
      delete amenities[amenityId];
    }

    // Update the h4 tag inside the div Amenities with the list of Amenities checked
    const amenitiesList = Object.values(amenities).join(', ');
    if (amenitiesList) {
      $('div.amenities > h4').text(amenitiesList);
    } else {
      $('div.amenities > h4').html('&nbsp;');
    }
  });
});
