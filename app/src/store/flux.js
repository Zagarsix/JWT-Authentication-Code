import { toast } from "react-toastify";
import Swal from "sweetalert2";
import { useNavigate } from "react-router-dom";

const getState = ({ getStore, getActions, setStore }) => {
  return {
    // Define all my variables
    store: {
      apiURL: "http://127.0.0.1:5000",
      email: "",
      password: "",
      currentUser: null,
    },
    // Define all my functions
    actions: {
      handleChange: (e) => {
        const { name, value } = e.target;
        setStore({
          [name]: value,
        });
      },
      handleLogin: async (e, navigate) => {
        e.preventDefault();

        const { apiURL, email, password } = getStore();

        const fields = {
          email: email,
          password: password,
        };

        // Fetching data from API
        const response = await fetch(`${apiURL}/api/login`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(fields),
        });

        const { status, message, data } = await response.json();

        console.log(data);

        // Display a certain notification based on status of the fetch data
        if (status === "failed") {
          toast.error(message);
        }
        if (status === "success") {
          Swal.fire({
            icon: "success",
            title: message,
            showConfirmButton: false,
            timer: 1500,
          });

          // Saving user data on session storage
          sessionStorage.setItem("currentUser", JSON.stringify(data));

          setStore({
            currentUser: data,
            // clear data if user sign out
            email: "",
            password: "",
          });

          navigate("/private");
        }
      },
      handleRegister: async (e, navigate) => {
        e.preventDefault();

        const { apiURL, email, password } = getStore();

        const fields = {
          email: email,
          password: password,
        };

        // Fetching data from API
        const response = await fetch(`${apiURL}/api/register`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(fields),
        });

        const { status, message, data } = await response.json();

        console.log(data);

        // Display a certain notification based on status of the fetch data
        if (status === "failed") {
          toast.error(message);
        }
        if (status === "success") {
          Swal.fire({
            icon: "success",
            title: message,
            showConfirmButton: false,
            timer: 1500,
          });

          // Saving user data on session storage
          sessionStorage.setItem("currentUser", JSON.stringify(data));

          setStore({
            currentUser: data,
            // clear password on login so if user goes to update profile, the password field is blank
            password: "",
          });

          navigate("/login");
        }
      },
      checkAuth: () => {
        if (sessionStorage.getItem("currentUser")) {
          setStore({
            currentUser: JSON.parse(sessionStorage.getItem("currentUser")),
          });
        }
      },
    },
  };
};

export default getState;
