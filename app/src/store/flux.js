import { toast } from "react-toastify";
import Swal from "sweetalert2";
import "react-toastify/dist/ReactToastify.css";

const getState = ({ getStore, getActions, setStore }) => {
  return {
    // Define all my variables
    store: {
      apiURL: "http://127.0.0.1:5000",
      email: "",
      password: "",
      store: null,
    },
    // Define all my functions
    actions: {
      handleChange: (e) => {
        const { name, value } = e.target;
        setStore({
          [name]: value,
        });
      },
      handleLogin: async (e) => {
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

        const data = await response.json();

        console.log(data);

        // Display a certain notification based on status of the fetch data
        if (data.status === "failed") {
          toast.error(data.message);
        }
        if (data.status === "success") {
          Swal.fire({
            position: "center",
            icon: "success",
            title: data.message,
            showConfirmButton: false,
            timer: 1500,
          });
        }
      },
    },
  };
};

export default getState;
