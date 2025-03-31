import jwt from "jsonwebtoken";
import User from "../models/user.model.js";

export const protectRoute = async (req, res, next) => {
    try {

        // retrieves jwt from user's browers cookies
        const token = req.cookies.jwt;

        // checks if token exists
        if (!token) {
            return res.status(401).json({ message: "Unauthorized - No Token Provided" });
        }

        const decoded = jwt.verify(token, process.env.JWT_SECRET);

        // checks if existing token is valid or not
        if (!decoded) {
            return res.status(401).json({ message: "Unauthorized - Invalid Token" });
        }

        // retrieves user from the decoded token
        const user = await User.findById(decoded.userId).select("-password");

        // checks if user exists
        if (!user) {
            return res.status(404).json({ message: "User not found" });
        }

        req.user = user;
        
        next();

    } catch (error) {
        console.log("Error in protectedRoute middleware: ", error.message);
        res.status(500).json({ message: "Internal Server Error" });
    }
}
