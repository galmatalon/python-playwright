import time

from playwright.sync_api import Page


class BasePage:
    def __init__(self, page:Page):
        self.__page = page

    def fill_text(self, locator, text):
        #self.__page.locator(locator).highlight()
        time.sleep(0.5)
        element = self.__page.locator(locator)
        element.evaluate("""
            el => {
                const origShadow = el.style.boxShadow;
                const origBackground = el.style.backgroundColor;

                el.style.boxShadow = '0 0 10px 4px rgba(0, 150, 255, 0.7)';
                el.style.backgroundColor = 'yellow';

                setTimeout(() => {
                    el.style.boxShadow = origShadow;
                    el.style.backgroundColor = origBackground;
                }, 300);
            }
        """)
        self.__page.locator(locator).fill(text)

    def click(self, locator):
        self.__page.locator(locator).highlight()
        self.__page.locator(locator).click()

    def select_option(self, locator, text):
        self.__page.locator(locator).select_option(value=text)


# Highlight element by changing background color
#         element = self.__page.locator(locator)
#         element.evaluate("""
#                el => {
#                    // Save original styles
#                    const originalBoxShadow = el.style.boxShadow;
#                    const originalTransform = el.style.transform;
#                    const originalTransition = el.style.transition;
#
#                    // Apply awesome effect
#                    el.style.transition = 'box-shadow 0.3s ease, transform 0.1s ease';
#                    el.style.boxShadow = '0 0 10px 4px rgba(0, 150, 255, 0.7)';
#                    el.style.transform = 'scale(1.05)';
#
#                    // Revert to original styles after effect
#                    setTimeout(() => {
#                        el.style.boxShadow = originalBoxShadow;
#                        el.style.transform = originalTransform;
#                        el.style.transition = originalTransition;
#                    }, 300);
#                }
#            """)

#
# element = self.__page.locator(locator)
#         element.evaluate("""
#             el => {
#                 const origShadow = el.style.boxShadow;
#                 el.style.boxShadow = '0 0 10px 4px rgba(0, 150, 255, 0.7)';
#                 setTimeout(() => el.style.boxShadow = origShadow, 300);
#             }
#         """)