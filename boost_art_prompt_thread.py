from PyQt6.QtCore import QThread, pyqtSignal
import openai

class BoostArtPromptThread(QThread):
    promptBoosted = pyqtSignal(str)

    def __init__(self, prompt):
        super().__init__()
        self.prompt = prompt

    def run(self):
        boosted_prompt = self.boost_art_prompt(self.prompt)
        self.promptBoosted.emit(boosted_prompt)

    def boost_art_prompt(self, prompt):
        # Define the boost instruction
        boost_instruction = "Craft an art prompt for DALL-E by transforming the following text into a powerful catalyst for awe-inspiring art:"

        # Combine the boost instruction with the existing prompt
        combined_prompt = f"{boost_instruction} {prompt}"

        # Use OpenAI to rewrite the art prompt and engineer the best prompt
        # You can customize this logic according to your requirements
        boosted_prompt = openai.Completion.create(
            engine="text-davinci-003",
            prompt=combined_prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=1.0,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        ).choices[0].text.strip()

        return boosted_prompt