const getState = ({ getStore, getActions, setStore }) => {
  return {
    // Define all my variables
    store: {
      email: "",
      password: "",
    },
    // Define all my functions
    actions: {
      handleChange: (e) => {
        const { name, value } = e.target;
        setStore({
          [name]: value,
        });
      },
    },
  };
};

export default getState;
