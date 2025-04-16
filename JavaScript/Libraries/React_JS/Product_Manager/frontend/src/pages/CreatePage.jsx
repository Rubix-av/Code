import React, { useState } from 'react'
import { useProductStore } from '../store/product';
import toast from 'react-hot-toast';

function CreatePage() {

  const [newProduct, setNewProduct] = useState({
    name: "",
    price: "",
    image: ""
  })

  const {createProduct} = useProductStore()
  
  const handleAddProduct = async() => {
    const {success, message} = await createProduct(newProduct);
    if(!success) {
      toast.error({message})
    } else {
      toast.success({message})
    }
    setNewProduct({ name: "", price: "", image: ""});
  };


  return (
    <div className="size-full h-screen flex justify-center">
      <div className="h-120 w-240 p-5 flex flex-col items-center">
        <div className="mb-10 text-6xl font-bold capitalize">create new product</div>
        <div className="bg-gray-800 p-5 w-180 rounded">

          {/* Product name input */}
          <label className="input w-full mb-5">
            <input type="search" className="grow input-xl" placeholder="Product Name" value={newProduct.name} onChange={e => setNewProduct({ ...newProduct, name: e.target.value})} />
          </label>

          {/* Product price input */}
          <label className="input w-full mb-5">
            <input type="text" className="grow input-xl" placeholder="Price" value={newProduct.price} onChange={e => setNewProduct({ ...newProduct, price: e.target.value})} />
          </label>

          {/* Product image url input */}
          <label className="input w-full mb-5">
            <input type="text" className="grow input-xl" placeholder="Image URL" value={newProduct.image} onChange={e => setNewProduct({ ...newProduct, image: e.target.value})} />
          </label>
          <button className="w-full bg-blue-300 p-2 text-black text-xl font-bold rounded cursor-pointer hover:bg-blue-400 transition-colors" onClick={handleAddProduct}>Add Product</button>

        </div>
      </div>
    </div>
  )
}

export default CreatePage