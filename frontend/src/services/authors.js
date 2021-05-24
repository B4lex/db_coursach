import api from '.'


export async function get_all_authors() {
    return await api.get('/authors').then(response => response.data)
}

export async function get_author_by_id(author_id) {
    return await api.get('/authors', {
        params: {
            id: author_id
        }
    }).then(response => {
        let data = response.data
        return data.length >= 1 ? data[0] : null
    })
}

export async function create_author(author_data) {
    return await api.post('authors', author_data).then(response => response.status)
}