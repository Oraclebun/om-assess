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
    
});