- `parseFloat(value)` is for turn the data into `float` format
- `toFixed(2)` is the same as `.2f` in C
- `innerText`, `innerHTML` and `textContent`
    - `innerHTML`: the browser will render **HTML tag**
    - `innerText`: the browser return text and **ignore** HTML tag, not show hidden text (`display: None`)
    - `textContent`: like `innerText` but faster and show hidden text

- DOM element is a element in HTML and you can extract properties of the element in JavaScript

- Button type:
    - `submit` will send the data(username=data)  to /submit
    - `reset` will reset all form of input 

- HTML `<form>`:
    - Where the data goes?
        - control by `action`
        ```html
        <form action="/signup" method="post">
            ...
        </form>
        ```
    - How the data is sent:
        - control by `method` attributes
        - `GET`: the data goes in the URL query string (send to JavaScript)
        - `POST`: go to request body (send to the server)

    - How to use `<form>` to get the input from the user to JavaScript:
        ```js
        // Get the form element
        const form = document.getElementbyId("idOfForm");

        //Listen when the form is submitted
        form.addEventListener("submit", function(event) {
            event.preventDefault();

            // Get all the form data
            const formData = new FormData(form);

            const username = formData.get("username");
            const email = formData.get("email");
        })
        ```
        - `function(event)` is a anonymous function that run when the `form` detect a `submit` button have been press.

    - If you press `Submit` button, it will reset the data, include the data in the input box and whipe down every data in JS


<h1>jQuery</h1>

- is a lightweight JavaScript library
- wrap many complicated JavaScript code into simple ones
- Use of jQuery:
    - HTML/DOM manipulator
    - CSS manipulator
    - HTML event method
    - Effects and animation
    - AJAX method

- Basic syntax 
```js 
$(selector).action() 
```
- use `$(#element)` to select element in the page that have the `id` = `element`
- `.attr(name)` to get the value of the attribute, `.attr(name, value)` to chagne the value of the attribute 
- `.text()` and `.text(text)` is same as `.attr()`
- `.val(id)` to get the element value by id
- `Date.now()` will get you the current time
- `#("element").click(function() {})` is equivalent as `document.getElementById("element").addEventListener("click", function() {})`
- `.ready()` is when the DOM structure is ready


<h1>Blur and Focus</h1>

- Is a state of a element, `focus` is when a element is ready to get a input and `blur` is the opposite
- Use `addEventListener("blur", some function doing something idk)` to send signal when the element is chagne state. 


<h2>jQuery AJAX</h2>

- `load(file)` to load data to a file
```js
$(document).ready(function() {
    $("button").click(function() {
        $("#div1").load("data.txt")
    })
})
```