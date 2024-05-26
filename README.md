# xanadude

xanadude is a modernized version of the classic Project Xanadu, updated to run on a variety of systems

## Inspiration

The inspiration behind xanadude comes from Project Xanadu®, which was founded in 1960 by Ted Nelson. Project Xanadu is the original hypertext project and aimed to create a universal network of interconnected documents. It was the first project to envision a world where all kinds of information could be easily linked together, pretty cool huh.

Project Xanadu introduced concepts such as visible connections (links) between documents, bi-directional links, and version management of information. These ideas morphed over the years into that thing called WWW or something like that!

For more information about Project Xanadu, visit [Xanadu's official website](https://xanadu.com/xUniverse-D6).

## Installation

1. Create and activate a virtual environment:

   ```bash
   python -m venv xanadude_env
   source xanadude_env/bin/activate  # On macOS/Linux: source xanadude_env/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install PyQt5 pathlib
   ```

## Running xanadude

1. Run the main application:

   ```bash
   python main.py
   ```

2. Check the logs in `logs/xanadude.log` for detailed information and debugging.

## Usage

- Navigate through the tabs to explore different functionalities:
  - **Home Tab:** Displays a welcome message and shows the result of input events.
  - **Input Tab:** Allows triggering of input events and logs the actions.
  - **Settings Tab:** Provides basic settings for the application.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
