const userForm = document.querySelector(".user");
const companyForm = document.querySelector(".company");
const userBtn = document.querySelector(".userBtn");
const companyBtn = document.querySelector(".companyBtn");

userBtn.addEventListener("click", () => {
    userForm.classList.remove("hidden");
    companyForm.classList.add("hidden");
    userBtn.classList.add("required");
    companyBtn.classList.remove("required");
})

companyBtn.addEventListener("click", () => {
    companyForm.classList.remove("hidden");
    userForm.classList.add("hidden");
    companyBtn.classList.add("required");
    userBtn.classList.remove("required");
})