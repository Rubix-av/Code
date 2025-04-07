import React, { useState } from 'react'

function CreatePage() {

  const [productName, setProductName] = useState("");
  const [productPrice, setProductPrice] = useState("");
  const [imgUrl, setImgUrl] = useState("");

  return (
    <div className="size-full h-screen flex justify-center">
      <div className="h-60 w-120 p-5 flex flex-col items-center">
        <div className="mb-10 text-4xl font-bold capitalize">create new product</div>
        <div className="bg-gray-800 p-5 w-115 rounded">

          {/* Product name input */}
          <label className="input w-full mb-3 h-8">
            <input type="search" className="grow" placeholder="Product Name" value={productName} onChange={e => setProductName(e.target.value)} />
          </label>

          {/* Product price input */}
          <label className="input w-full mb-3 h-8">
            <input type="text" className="grow" placeholder="Price" value={productPrice} onChange={e => setProductPrice(e.target.value)} />
          </label>

          {/* Product image url input */}
          <label className="input w-full mb-3 h-8">
            <input type="text" className="grow" placeholder="Image URL" value={imgUrl} onChange={e => setImgUrl(e.target.value)} />
          </label>
          <button className="w-full bg-blue-300 p-2 text-black text-xs font-bold rounded cursor-pointer">Add Product</button>

        </div>
      </div>
    </div>
  )
}

export default CreatePage