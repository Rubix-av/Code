
function List(props) {

    const category = props.category
    const itemList = props.items

    // fruits.sort((a, b) => a.name.localeCompare(b.name)) // Alphabetical order
    // fruits.sort((a, b) => b.name.localeCompare(a.name)) // Reverse alphabetical order
    // fruits.sort((a,b) => a.calories - b.calories) // Numeric order
    // fruits.sort((a,b) => b.calories - a.calories) // Reverse numeric order

    const listItems = itemList.map(item => <li key={item.id}>
                                            {item.name}: &nbsp; <b>{item.calories}</b></li>)

    return (
        <>
            <h3 className="list-category">{category}</h3>
            <ol className="list-items">{listItems}</ol>
        </>
    );
}

export default List
