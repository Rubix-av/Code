import { generateToken } from "../lib/utils.js";
import User from "../models/user.model.js";
import bcrypt from "bcryptjs";
import cloudinary from "../lib/cloudinary.js"

export const signup = async (req, res) => {

    // req.body stores the data sent by user with POST method
    // fullName is basically like saying req.body.fullName, similarly with other fields
    const {fullName, email, password} = req.body;
    try {

        // checks if any of the field is empty
        if (!fullName || !email || !password) {
            return res.status(400).json({ message: "All fields are required" })
        }

        // checks for password length
        if (password.length < 6) {
            return res.status(400).json({ message: "Password must be atleast 6 characters"});
        }
        
        // tries to find a user with the passed email
        const user = await User.findOne({email});

        // if user with the passed email exists then send 400 error message
        if (user) return res.status(400).json({ message: "Email already exists" });
        
        // At this point, most of the checks are complete, and from below here, process to create user will be started
        // creates a bcrypt salt and hashes the password with the salt
        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(password, salt);

        // creates a newUser with passed details
        const newUser = new User({
            fullName,
            email,
            password: hashedPassword
        })

        // if newUser is defined properly, then generate token for newUser._id and save the newUser
        if (newUser) {
            generateToken(newUser._id, res);
            await newUser.save();

            // sends newUser data with 201 success message
            res.status(201).json({
                _id: newUser._id,
                fullName: newUser.fullName,
                email: newUser.email,
                profilePic: newUser.profilePic,
            })
        } else {
            res.status(400).json({ message: "Invalid user data" });
        }
    }

    // catches any error thrown by the try block
    catch (error) {
        console.log("Error in signup controller", error.message);
        res.status(500).json({ message: "Internal Server Error" });
    }
}

export const login = async (req, res) => {
    
    // gets data sent by user in req.boyd
    const { email, password } = req.body;
    try {

        // retrieves user with the passed email
        const user = await User.findOne({email});

        // checks if user with the passed email while login exists or not
        if (!user) {
            return res.status(400).json({ message: "Invalid credentials" })
        }

        // checks if password is correct or incorrect
        const isPasswordCorrect = await bcrypt.compare(password, user.password);
        if (!isPasswordCorrect) {
            return res.status(400).json({ message: "Invalid credentials" })
        }

        // generates token for user with user._id
        generateToken(user._id, res);

        // sends logged in users data with 200 success code
        res.status(200).json({
            _id: user._id,
            fullName: user.fullName,
            email: user.email,
            profilePic: user.profilePic
        })
        
    } catch (error) {
        console.log("Error in login controller", error.message);
        res.status(500).json({ message: "Internal Server Error" });
    }
}

export const logout = (req, res) => {
    try {
        res.cookie("jwt", "", {maxAge:0});
        res.status(200).json({ message: "Logged out successfully" });
    } catch (error) {
        console.log("Error in logout controller", error.message);
        res.status(500).json({ message: "Internal Server Error" });
    }
};

export const updateProfile = async (req, res) => {
    try {
        const { profilePic } = req.body;
        const userId = req.user._id;

        if (!profilePic) {
            return res.status(400).json({ message: "Profile pic is required" });
        }

        const uploadResponse = await cloudinary.uploader.upload(profilePic);
        const updatedUser = User.findByIdAndUpdate(userId, {profilePic:uploadResponse.secure_url}, {new:true})

        res.status(200).json(updatedUser);

    } catch (error) {
        console.log("Error in update profile: ", error);
        res.status(500).json({ message: "Internal Server Error" } );
    }
}

export const checkAuth = (req, res) => {
    try {
        res.status(200).json(req.user);
    } catch (error) {
        console.log("Error in checkAuth controller", error.message);
        res.status(500).json({ message: "Internal Server Error" });
    }
}
