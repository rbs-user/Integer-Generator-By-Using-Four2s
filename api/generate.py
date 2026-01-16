from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class IntegerFromNestedSqrt:
    def __init__(self, n: int):
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        self.n = n

    def generate_proof(self):
        """
        Returns a dictionary containing proof steps and final output.
        """
        proof_steps = [
            f"1) User input: n = {self.n}",
            f"2) Construct nested square-root expression: sqrt(sqrt(...sqrt(2))) applied {self.n} times, equals 2^(1 / 2^{self.n})",
            f"3) Inner logarithm: log2(2^(1 / 2^{self.n})) = 1 / 2^{self.n} = 2^-{self.n}",
            f"4) Outer logarithm: log2(2^-{self.n}) = -{self.n}",
            f"5) Apply leading minus: -(-{self.n}) = {self.n}",
            f"Conclusion: output equals input."
        ]
        return {
            "proof": proof_steps,
            "output": self.n
        }

@app.post("/generate")
async def generate_integer(user_input: str = Form(...)):
    try:
        n = int(user_input.strip())
        generator = IntegerFromNestedSqrt(n)
        result = generator.generate_proof()
        return JSONResponse(content=result)
    except ValueError:
        return JSONResponse(content={"error": "Invalid input. Please enter an integer."}, status_code=400)
