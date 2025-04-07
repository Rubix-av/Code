import { ShoppingCart, SquarePlus, SunMedium } from "lucide-react"

function Navbar() {
  return (
    <nav className="flex justify-between m-2 mb-4">
      <div className="flex">
        <div className="font-bold bg-gradient-to-r from-blue-500 to-purple-500 text-transparent bg-clip-text pr-2">  
          PRODUCT STORE 🛒
        </div>
      </div>
      
      <div className="join space-x-2">
        <div className="bg-gray-700 p-2 px-3 rounded"><SquarePlus className="size-4" /></div>
        <div className="bg-gray-700 p-2 px-3 rounded"><SunMedium className="size-4" /></div>
      </div>
    </nav>
  )
}

export default Navbar;
