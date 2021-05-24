import api from '.'


export async function get_all_books() {
    return await api.get('/books').then(response => response.data)
}

export async function get_book_by_id(book_id) {
    return await api.get('/books', {
        params: {
            id: book_id
        }
    }).then(response => response.data)
}

export async function create_book(book_data) {
    return await api.post('/books', book_data).then(response => response.status)
}