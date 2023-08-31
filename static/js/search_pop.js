new Autocomplete('#autocomplete', {
        search : input =>{
            console.log(input)
            const url = `/catalog/search_products/?search=${input}`
            return new Promise(resolve => {
                fetch(url)
                .then(response=>response.json())
                .then(data=>{
                console.log(data.payload)
                    resolve(data.data)
                })
            })
        },
        renderResult : (result, props) => {
            console.log(props)
            let group = ''
            if (result.index % 1 == 0){
            group = `<li class="group">Group</li>`
            }
            return `
            ${group}
            <li ${props}>
                <div class="wiki-title"
                    ${result.name}
                </div>
            </li>
            `
        }
    })