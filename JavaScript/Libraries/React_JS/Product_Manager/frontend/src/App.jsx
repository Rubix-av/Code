import { ShoppingCart, SquarePlus, Sun } from "lucide-react";
import Navbar from './components/Navbar.jsx';
import { Route, Routes } from "react-router-dom";
import HomePage from "./pages/HomePage.jsx"
import CreatePage from "./pages/CreatePage.jsx"
import { Toaster } from "react-hot-toast";

function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/create" element={<CreatePage />} />
      </Routes>

      <Toaster />
    </>
  )
}

export default App