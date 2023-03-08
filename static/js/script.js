let ingredientCount = 1;

document.getElementById("add_ingredient").addEventListener("click", function() {
    ingredientCount++;
    const newIngredientDiv = document.createElement("div");
    newIngredientDiv.classList.add("ingredient");

    const newLabel = document.createElement("label");
    newLabel.setAttribute("for", "ingredient_name_" + ingredientCount);
    newLabel.textContent = "Ingredient " + ingredientCount + ":";

    const newInput = document.createElement("input");
    newInput.setAttribute("type", "text");
    newInput.setAttribute("id", "ingredient_name_" + ingredientCount);
    newInput.setAttribute("name", "ingredient_name[]");
    newInput.required = true;

    newIngredientDiv.appendChild(newLabel);
    newIngredientDiv.appendChild(newInput);
    document.getElementById("ingredients-container").appendChild(newIngredientDiv);
});


let stepCount = 1;
const addStepButton = document.getElementById("add_step");
const stepsContainer = document.getElementById("steps-container");

addStepButton.addEventListener("click", function() {
    stepCount++;

    const newStepDiv = document.createElement("div");
    newStepDiv.classList.add("step");

    const newStepLabel = document.createElement("label");
    newStepLabel.textContent = "Step " + stepCount + ":";

    const newStepInstructionTextarea = document.createElement("textarea");
    newStepInstructionTextarea.setAttribute("id", "step_instruction_" + stepCount);
    newStepInstructionTextarea.setAttribute("name", "step_instruction[]");
    newStepInstructionTextarea.required = true;

    newStepDiv.appendChild(newStepLabel);
    newStepDiv.appendChild(newStepInstructionTextarea);
    stepsContainer.appendChild(newStepDiv);
});

const dairyFreeCheckbox = document.getElementById('dairy_free_checkbox');
  const dairyFreeHidden = document.getElementById('dairy_free_hidden');
  dairyFreeCheckbox.addEventListener('change', () => {
    dairyFreeHidden.value = dairyFreeCheckbox.checked ? 'on' : 'off';
  });