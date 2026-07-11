// Init empty array to store books
const library = []

// Books object constructor
function Books(title, author, pages, read){
    this.title = title
    this.author = author
    this.pages = pages
    this.read = read
}

// Function to create books based on user input and push them to library array
const title = document.getElementById('title')
const author = document.getElementById('author')
const pages = document.getElementById('pages')
const read = document.getElementById('read')

function addBookToLibrary(title, author, pages, read){
    const newBook = new Books(title, author, pages, read);
    newBook.id = crypto.randomUUID();
    library.push(newBook);
}

// Function to loop library array and display books on page
function displayBooks(){
    const container = document.querySelector('.library');
    container.innerHTML = "";
    library.forEach((book) => {
        const card = document.createElement('div')
        card.classList.add('book-card')
        // Add book info to card
        card.innerHTML = `
            <h2>${book.title}</h2>
            <p><strong>Author:</strong> ${book.author}</p>
            <p><strong>Pages:</strong> ${book.pages}</p>
            <p class="status">${book.read}</p>
        `;
        container.appendChild(card)
    });
}


// Event listeners for add book button
const addBook = document.getElementById('add')



