const update_Header = document.querySelector("#update_header");

update_Header.addEventListener("click", () => {
    document.querySelector("header").textContent = "New Header!!!";
});