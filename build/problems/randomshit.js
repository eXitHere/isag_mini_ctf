isVisible = false;

form = document.getElementById("form-submit");
input = document.getElementById("green");
input.addEventListener("change", handleChange);
let input2 = "";
function handleChange(e) {
  input2 = e.target.value;
}
document.getElementById("visible").addEventListener("click", function () {
  isVisible = !isVisible;
  if (!isVisible) {
    form.className = "d-none";
  } else {
    form.className = "";
  }
});
document.getElementById("unreal").addEventListener("click", function () {
  alert("https://www.youtube.com/watch?v=djV11Xbc914");
});
function gimmeDaCode() {
  console.log("SVNBR19GTEFHX0JVVF9OT1RfWUVU");
}
function handleSubmit(e) {
  if (input2 === "ISAG_FLAG_BUT_NOT_YET") {
    alert("ISAG{(*&@#!NICE(!@&!@ONE#))}");
  } else {
    alert("Nice try !!");
  }
}
