import api from '.'


export async function get_all_readers() {
    return await api.get('/persons').then(response => response.data)
}

export async function get_reader_books(reader_id) {
    return await api.get(`/persons`, {
        params: {
            id: reader_id, 
            related: 'books'
        }
    }).then(response => response.data)
}

export async function create_reader(reader_data) {
    return await api.post('/persons', reader_data).then(response => response.status)
}