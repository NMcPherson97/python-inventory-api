// Books object constructor
function Books(title, author, pages, read){
    this.title = title
    this.author = author
    this.pages = pages
    this.read = read
}

// Init empty array to store books
let library = []

// Function to create books based on user input and push them to library array
function addBookToLibrary(){
const userInputs = document.querySelectorAll('input, select')
const formValues = {};
  
// // Read values dynamically
userInputs.forEach(input => {
    if(input.name){
        formValues[input.name] = input.value
    }});

const newBook = new Books(
    formValues.title, 
    formValues.author, 
    formValues.pages, 
    formValues.read)
newBook.id = crypto.randomUUID()
library.push(newBook)}


// Function to loop library array. Display and Delete books on page
function displayAndDeleteBooks(){
    const container = document.querySelector('.library');
    container.innerHTML = "";
    library.forEach((book) => {
        const card = document.createElement('div')
        card.classList.add('book-card')
        card.id = book.id

        // // Add book info to card
        card.innerHTML = `
            <h2>${book.title}</h2>
            <p><strong>Author:</strong> ${book.author}</p>
            <p><strong>Pages:</strong> ${book.pages}</p>
            <p class="status">${book.read}</p>
        `
        const removeBook = document.createElement('button')
        removeBook.innerHTML = 'Remove Book'

        removeBook.addEventListener('click', () => {
        library = library.filter(b => b.id !== book.id);
        displayAndDeleteBooks();
        });

        const toggleRead = document.createElement('select')
        toggleRead.classList.add('toggle-btn')
        toggleRead.value = book.read
        toggleRead.innerHTML = `
            <option>Status</option>
            <option>Read</option>
            <option>Reading</option>
            <option>Want to Read</option>`
        toggleRead.addEventListener('change',(e)=>{
            book.read = e.target.value
            displayAndDeleteBooks()
        })

        card.append(toggleRead)
        card.appendChild(removeBook)
        container.appendChild(card)
        })       
    };

// Event listeners for add book button
const bookForm = document.querySelector('form')
const addBook = document.getElementById('add')

addBook.addEventListener('click',(e)=>{
    e.preventDefault()
    addBookToLibrary()
    displayAndDeleteBooks()
    bookForm.reset()    
    console.log(library)
})













