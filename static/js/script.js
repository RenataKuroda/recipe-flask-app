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

    const deleteIngButton = document.createElement("button");
    deleteIngButton.textContent = "x";
    deleteIngButton.classList.add("delete-button");

    newIngredientDiv.appendChild(newLabel);
    newIngredientDiv.appendChild(newInput);
    document.getElementById("ingredients-container").appendChild(newIngredientDiv);
    newIngredientDiv.appendChild(deleteIngButton);

    deleteIngButton.addEventListener("click", function() {
        newIngredientDiv.remove();
        ingredientCount--;
    });
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

    const newStepInstructionInput = document.createElement("input");
    newStepInstructionInput.setAttribute("type", "text");
    newStepInstructionInput.setAttribute("id", "step_instruction_" + stepCount);
    newStepInstructionInput.setAttribute("name", "step_instruction[]");
    newStepInstructionInput.required = true;

    const deleteStepButton = document.createElement("button");
    deleteStepButton.textContent = "x";
    deleteStepButton.classList.add("delete-button");

    newStepDiv.appendChild(newStepLabel);
    newStepDiv.appendChild(newStepInstructionInput);
    stepsContainer.appendChild(newStepDiv);
    newStepDiv.appendChild(deleteStepButton);

    deleteStepButton.addEventListener("click", function() {
        newStepDiv.remove();
        stepCount--;
    });
});
