from argparse import Namespace
from typing import Dict
from pathlib import Path

from .question import Question
from .session import Session
from .participant import Participant

QUESTIONS_FOLDER = Path('questions')

class AppContext:
    args = Namespace(
        mqtt_port=1883,
        api_port=5000,
    )

    mqtt_broker = None
    api_service = None

    sessions: 'Dict[Session]' = {}
    questions: 'Dict[Question]' = {}

    @staticmethod
    def reload_questions():
        AppContext.questions = {
        question.id: question for question in filter(
            lambda question: question is not None,
            map(
                lambda question_path: Question.from_folder(question_path),
                QUESTIONS_FOLDER.iterdir()
            )
        )
    }