/**
 * static/js/new_picture.js
 *
 *
 */

function changePicture()
{
    /* file dialog */
    /* user id */
    console.log("changePicture");
    
    $("#id_member_img").click()
}

function setStandardPicture()
{
    /* */
    console.log("setStandardPicture");

    $("#id_image").attr("src", "/member/img/0");
}

function loadFile(evt)
{
    image=evt.target.files[0];
    if (image.type.match("image/*")) {
	var reader = new FileReader();
	reader.onload = function(e) {
	    // TODO bild verkleinern und speichern als png
	    $("#id_image").attr("src", e.target.result);
	};
	reader.readAsDataURL(image);
    }
    console.log("loadFile");
}
