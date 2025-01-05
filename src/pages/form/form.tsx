import React, { useState } from "react";

type User = {
    username: string;
    password: string;
};

const Form: React.FC = () => {
    const [user, setUser] = useState<User>({ username: "", password: "" });
    const [error, setError] = useState<string | null>(null);

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setUser((prevUser) => ({
            ...prevUser,
            [name]: value,
        }));
    };

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        // try {
        //     const response = await fetch('http://127.0.0.1:5000/add_user', {
        //         method: 'POST',
        //         headers: {
        //             'Content-Type': 'application/json', // Specify content type
        //         },
        //         body: JSON.stringify(user), // Convert user object to JSON
        //     });

        //     if (!response.ok) {
        //         throw new Error('Network response was not ok');
        //     }

        //     const json = await response.json();
        //     console.log("User submitted:", json);
        //     setUser({ username: "", password: "" }); // Reset form fields
        //     setError(null); // Clear any previous errors
        // } catch (error) {
        //     console.error("Error submitting user:", error);
        //     setError("Failed to submit user"); // Set error message
        // }
        console.log(user)
    };

    return (
        <>
            <form className="max-w-sm mx-auto" onSubmit={handleSubmit}>
                <div className="mb-5">
                    <label htmlFor="username" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                        Your email
                    </label>
                    <input
                        type="email"
                        id="username"
                        name="username" 
                        value={user.username}
                        onChange={handleChange}
                        className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        placeholder="name@flowbite.com"
                        required
                    />
                </div>
                <div className="mb-5">
                    <label htmlFor="password" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                        Your password
                    </label>
                    <input
                        type="password"
                        id="password"
                        name="password" 
                        value={user.password}
                        onChange={handleChange}
                        className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        required
                    />
                </div>
                <div className="flex items-start mb-5">
                    <div className="flex items-center h-5">
                        <input
                            id="remember"
                            type="checkbox"
                            value=""
                            className="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800"
                            required
                        />
                    </div>
                    <label htmlFor="remember" className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                        Remember me
                    </label>
                </div>
                {error && <p className="text-red-500">{error}</p>} 
                <button
                    type="submit"
                    className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                >
                    Submit
                </button>
            </form>
        </>
    );
};

export default Form;