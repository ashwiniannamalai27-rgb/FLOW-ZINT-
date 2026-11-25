const chart=document.getElementById("financeChart");

const budget=Number(chart.dataset.budget);

const expense=Number(chart.dataset.expense);

const savings=Number(chart.dataset.savings);

new Chart(chart,{

type:"bar",

data:{

labels:["Budget","Expense","Savings"],

datasets:[{

label:"Amount",

data:[budget,expense,savings],

backgroundColor:[

"#3b82f6",

"#ef4444",

"#10b981"

],

borderRadius:15,

borderSkipped:false

}]

},

options:{

responsive:true,

plugins:{

legend:{

display:false

}

},

scales:{

y:{

beginAtZero:true,

grid:{

color:"rgba(255,255,255,.1)"

},

ticks:{

color:"white"

}

},

x:{

ticks:{

color:"white"

},

grid:{

display:false

}

}

}

}

});