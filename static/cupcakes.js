const baseAPI = "/api/cupcakes";
const form = document.querySelector('#cupcakeform');
const flavor = document.querySelector('input[name="flavor"]');
const size = document.querySelector('input[name="size"]');
const rating = document.querySelector('input[name="rating"]');
const image = document.querySelector('input[name="image-url"]');
const cupcakeList = document.querySelector('#cupcakelist');
let ul = document.querySelector("ul");
let newLi = document.createElement('li');


async function getCupcakes() {
    const response = await axios.get(baseAPI); // This code will run and it will wait until we get a value
    console.log(response);
}

$("#submit").on("click", async function createCupcake(evt) {
    evt.preventDefault();

    const formInput = {
        flavor: flavor.value,
        size: size.value,
        rating: rating.value,
        image: image.value,
    };
    
    const response = await axios.post(baseAPI, formInput);
    newLi.innerText = `${formInput.flavor} ${formInput.size} ${formInput.rating} ${formInput.image}`;
    ul.append(newLi);
});

