from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers.string import StrOutputParser
import os
from third_parties.linkedin import scrap_linkedin_profile


if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain")
    print(os.environ["OPENAI_API_KEY"])

    summary_template = """Given the linked information {information} about a person from i want you to create:
                        1.a short summary
                        2.two interesting facts about them
                        """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    #llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm=ChatOllama(model="llama3")

    chain = summary_prompt_template | llm | StrOutputParser()
    information = scrap_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/anish-singh-32586540/')
    res = chain.invoke(input={"information": information})
    print(res)
