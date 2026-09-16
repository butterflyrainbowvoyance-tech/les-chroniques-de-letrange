import "@/App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Toaster } from "sonner";
import { FavoritesProvider } from "@/context/FavoritesContext";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import HomePage from "@/pages/HomePage";
import UniversePage from "@/pages/UniversePage";
import StoryPage from "@/pages/StoryPage";
import TimelinePage from "@/pages/TimelinePage";
import MapPage from "@/pages/MapPage";
import RandomPage from "@/pages/RandomPage";
import QuizPage from "@/pages/QuizPage";
import FavoritesPage from "@/pages/FavoritesPage";
import SearchPage from "@/pages/SearchPage";
import VoyagePage from "@/pages/VoyagePage";
import VoyageEraPage from "@/pages/VoyageEraPage";

function App() {
  return (
    <FavoritesProvider>
      <div className="App bg-grain min-h-screen relative">
        <BrowserRouter>
          <Navbar />
          <main className="relative z-10 pt-20">
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/univers/:universeId" element={<UniversePage />} />
              <Route path="/recit/:storyId" element={<StoryPage />} />
              <Route path="/frise" element={<TimelinePage />} />
              <Route path="/carte" element={<MapPage />} />
              <Route path="/etrange" element={<RandomPage />} />
              <Route path="/quiz" element={<QuizPage />} />
              <Route path="/bibliotheque" element={<FavoritesPage />} />
              <Route path="/recherche" element={<SearchPage />} />
              <Route path="/voyage" element={<VoyagePage />} />
              <Route path="/voyage/:eraId" element={<VoyageEraPage />} />
            </Routes>
          </main>
          <Footer />
        </BrowserRouter>
        <Toaster theme="dark" position="bottom-right" />
      </div>
    </FavoritesProvider>
  );
}

export default App;
