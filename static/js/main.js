document.addEventListener("DOMContentLoaded", function(event) {
    // on DOM ready

const planSelectElement = document.querySelector('#inputPlan'); //select input for plan
const periodSelectElement = document.querySelector('#inputPeriod'); //select input for period
let planSelectedIndex = planSelectElement.selectedIndex;        // get selected plan
let periodSelectedIndex = periodSelectElement.selectedIndex;    //get selected period

if(sessionStorage.getItem('planSelectedIndex')){
    planSelectElement.selectedIndex=sessionStorage.getItem('planSelectedIndex');    
}

if(sessionStorage.getItem('periodSelectedIndex')){
    periodSelectElement.selectedIndex=sessionStorage.getItem('periodSelectedIndex');    
}

//planSelectElement.addEventListener('change', (event) => {
//    sessionStorage.setItem('planSelectedIndex',event.target.selectedIndex);
    //event.target.form.submit();
  
//});

//periodSelectElement.addEventListener('change', (event) => {
//    sessionStorage.setItem('periodSelectedIndex',event.target.selectedIndex);
//    //event.target.form.submit();
  
//});

//if the selected plan is CRM Sol only,
if (planSelectedIndex == 2){
// Get a reference to the parent node

let parentDiv = [];
let eDocNum = [];
let subAcc = [];
for (let i = 0; i < 3; i++) {
    // Get parent node of elements with e-doc info
    parentDiv[i] = document.getElementsByClassName("e-doc")[i].parentNode;
    //Get all the elements with e-doc info
    eDocNum[i] = document.getElementsByClassName("e-doc")[i];
    //Get all the elements with sub-account info
    subAcc[i] = document.getElementsByClassName("sub-acc")[i];
    parentDiv[i].insertBefore(subAcc[i], eDocNum[i]);
}

}


});