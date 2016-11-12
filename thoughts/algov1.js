//Savings algo

// this is for a known bump with static Y, m & std_dev

// bump
var income = 300;

// historic data
var avg_income = 100;
var std_dev = 25;
var origin = avg_income - std_dev;
var constant = 0.05; // arbitrary amount, should eventually be generated relating to savings goal

// last dollar distance

var dist = income - origin;

// calculate saving
var height = (((income - origin) / std_dev) * constant); // amount saved for the last dollar
var base = income - origin;
var savings_rec = 0.5 * base * height;

// correcting for outliers

if (savings_rec <= 0) {
  savings_rec = 0;
} // corrects for lower bounds

var savings_ratio = savings_rec / income

if (savings_pct >= 0.4) {
  savings_rec = income * 0.4;
} // corrects for upwards bounds
