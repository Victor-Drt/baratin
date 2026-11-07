import "./styles.css";

const RegisterPage = () => {

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    const name = formData.get("name") as string;
    const email = formData.get("email") as string;
    const password = formData.get("password") as string;

    // Aqui você pode fazer a lógica de registro, como enviar os dados para o backend
    console.log("Nome:", name);
    console.log("Email:", email);
    console.log("Senha:", password);
  };

  return (
    <main className="register-page">
      <section className="card-form-register">
        <h1>Register Page</h1>

        <form onSubmit={handleSubmit}>
          <div className="form-row">
            <label htmlFor="name">Name</label>
            <input type="text" id="name" name="name" required />
          </div>
          <div className="form-row">
            <label htmlFor="email">Email</label>
            <input type="email" id="email" name="email" required />
          </div>
          <div className="form-row">
            <label htmlFor="password">Password</label>
            <input type="password" id="password" name="password" required />
          </div>
          <button type="submit">Register</button>
        </form>
      </section>

      <section className="card-image-register">
        <img src="https://placehold.co/600x400" alt="Imagem de Placeholder" />
      </section>
    </main>
  );
};

export default RegisterPage;
