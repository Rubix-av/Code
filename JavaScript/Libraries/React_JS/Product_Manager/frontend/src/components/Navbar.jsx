import { ShoppingCart, SquarePlus, SunMedium } from "lucide-react"

function Navbar() {
  return (
    <nav className="flex justify-between m-2 mb-8">
      <div className="flex">
        <div className="font-bold bg-gradient-to-r from-blue-500 to-purple-500 text-transparent bg-clip-text pr-2 text-3xl">  
          PRODUCT STORE 🛒
        </div>
      </div>
      
      <div className="join space-x-2">
        <div className="bg-gray-700 hover:bg-gray-800 transition-colors p-2 px-3 cursor-pointer rounded"><SquarePlus className="size-7" /></div>
        <div className="bg-gray-700 hover:bg-gray-800 transition-colors p-2 px-3 cursor-pointer rounded"><SunMedium className="size-7" /></div>
      </div>
    </nav>
  )
}

export default Navbar;
