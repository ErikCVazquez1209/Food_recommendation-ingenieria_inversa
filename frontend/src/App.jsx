import { useState } from 'react'
import './App.css'


const API_URL = 'http://127.0.0.1:8000'

const INITIAL_FORM = {
  foodType: 'Healthy',
  maxMinutes: '30',
  maxSteps: '6',
  maxIngredients: '8',
}


function App() {
  const [formData, setFormData] = useState(INITIAL_FORM)
  const [recipe, setRecipe] = useState(null)
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  function handleChange(event) {
    const { name, value } = event.target

    setFormData((currentData) => ({
      ...currentData,
      [name]: value,
    }))
  }

  async function handleSubmit(event) {
    event.preventDefault()

    setLoading(true)
    setRecipe(null)
    setError('')

    const requestData = {
      food_type: formData.foodType,
      max_minutes: Number(formData.maxMinutes),
      max_steps: Number(formData.maxSteps),
      max_ingredients: Number(formData.maxIngredients),
    }

    try {
      const response = await fetch(
        `${API_URL}/api/recommendations`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(requestData),
        },
      )

      const responseData = await response.json()

      if (!response.ok) {
        if (response.status === 404) {
          setError(
            'No encontramos una receta que cumpla todos los límites.',
          )
        } else {
          setError(
            'Los datos proporcionados no son válidos.',
          )
        }

        return
      }

      setRecipe(responseData)
    } catch {
      setError(
        'No fue posible conectarse con el servidor.',
      )
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="app-shell">
      <section className="intro">
        <p className="eyebrow">
          FastAPI + React
        </p>

        <h1>Food Recommendation</h1>

        <p>
          Selecciona una categoría y establece los límites
          máximos de la receta.
        </p>
      </section>

      <section className="form-card">
        <form onSubmit={handleSubmit}>
          <div className="form-grid">
            <label>
              Categoría
              <select
                name="foodType"
                value={formData.foodType}
                onChange={handleChange}
              >
                <option value="Healthy">
                  Saludable
                </option>

                <option value="Veg">
                  Vegetariana
                </option>

                <option value="Non-Veg">
                  No vegetariana
                </option>

                <option value="Veg_Dessert">
                  Postre vegetariano
                </option>

                <option value="Non-Veg_Dessert">
                  Postre no vegetariano
                </option>
              </select>
            </label>

            <label>
              Minutos máximos
              <input
                type="number"
                name="maxMinutes"
                min="1"
                value={formData.maxMinutes}
                onChange={handleChange}
                required
              />
            </label>

            <label>
              Pasos máximos
              <input
                type="number"
                name="maxSteps"
                min="1"
                value={formData.maxSteps}
                onChange={handleChange}
                required
              />
            </label>

            <label>
              Ingredientes máximos
              <input
                type="number"
                name="maxIngredients"
                min="1"
                value={formData.maxIngredients}
                onChange={handleChange}
                required
              />
            </label>
          </div>

          <button
            type="submit"
            disabled={loading}
          >
            {loading
              ? 'Buscando...'
              : 'Recomendar receta'}
          </button>
        </form>

        {error && (
          <p
            className="error-message"
            role="alert"
          >
            {error}
          </p>
        )}
      </section>

      {recipe && (
        <section
          className="recipe-card"
          aria-live="polite"
        >
          <div className="recipe-heading">
            <div>
              <p className="eyebrow">
                Recomendación
              </p>

              <h2>{recipe.name}</h2>
            </div>

            <span className="score">
              ★ {recipe.score}
            </span>
          </div>

          <div className="recipe-data">
            <span>
              {recipe.food_type}
            </span>

            <span>
              {recipe.minutes} minutos
            </span>

            <span>
              {recipe.ingredients.length} ingredientes
            </span>
          </div>

          <div className="recipe-columns">
            <div>
              <h3>Ingredientes</h3>

              <ul>
                {recipe.ingredients.map((ingredient) => (
                  <li key={ingredient}>
                    {ingredient}
                  </li>
                ))}
              </ul>
            </div>

            <div>
              <h3>Preparación</h3>

              <ol>
                {recipe.steps.map((step) => (
                  <li key={step}>
                    {step}
                  </li>
                ))}
              </ol>
            </div>
          </div>
        </section>
      )}
    </main>
  )
}

export default App