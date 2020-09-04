document.addEventListener("DOMContentLoaded", function(event) {
    // on DOM ready

const planSelectElement = document.querySelector('#inputPlan'); //select input for plan
const periodSelectElement = document.querySelector('#inputPeriod'); //select input for period
let planSelectedIndex = planSelectElement.selectedIndex;
let periodSelectedIndex = periodSelectElement.selectedIndex;

if(localStorage.getItem('planSelectedIndex')){
    planSelectElement.selectedIndex=localStorage.getItem('planSelectedIndex');    
}

if(localStorage.getItem('periodSelectedIndex')){
    periodSelectElement.selectedIndex=localStorage.getItem('periodSelectedIndex');    
}

planSelectElement.addEventListener('change', (event) => {
    localStorage.setItem('planSelectedIndex',event.target.selectedIndex);
    event.target.form.submit();
  
});

periodSelectElement.addEventListener('change', (event) => {
    localStorage.setItem('periodSelectedIndex',event.target.selectedIndex);
    event.target.form.submit();
  
});


//if the selected plan is CRM Sol only,
if (planSelectedIndex = 2){
// Get a reference to the parent node
let parentDiv0 = document.getElementsByClassName("e-doc")[0].parentNode;
let parentDiv1 = document.getElementsByClassName("e-doc")[1].parentNode;
let parentDiv2 = document.getElementsByClassName("e-doc")[2].parentNode;

//Get all the elements with e-doc info
let eDocNum0 = document.getElementsByClassName("e-doc")[0];
let eDocNum1 = document.getElementsByClassName("e-doc")[1];
let eDocNum2 = document.getElementsByClassName("e-doc")[2];

//Get all the elements with sub-account info
let subAcc0 = document.getElementsByClassName("sub-acc")[0];
let subAcc1 = document.getElementsByClassName("sub-acc")[1];
let subAcc2 = document.getElementsByClassName("sub-acc")[2];

//move the location of sub-account before e-doc
parentDiv0.insertBefore(subAcc0, eDocNum0);
parentDiv1.insertBefore(subAcc1, eDocNum1);
parentDiv2.insertBefore(subAcc2, eDocNum2);
}


});